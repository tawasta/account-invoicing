from odoo import models
from odoo import _
from odoo import SUPERUSER_ID


class QueueJobBatch(models.Model):

    _inherit = "queue.job.batch"

    def check_state(self):
        pre_state = self.state

        res = super().check_state()

        if (
            pre_state != "finished"
            and self.job_ids
            and self.job_ids[0].job_function_id
            and self.job_ids[0].job_function_id.method == "create_commission_payment"
        ):
            if self.state == "finished":
                msg = _(
                    "Batch of {} jobs completed: {}".format(
                        self.finished_job_count, self.name
                    )
                )
                self.message_post(
                    body=msg,
                    message_type="comment",
                    subtype_xmlid="mail.mt_comment",
                    notify_by_email=True,
                    author_id=SUPERUSER_ID,
                )
        return res
