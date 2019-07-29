from django.db import models
from datetime import datetime

class Frank(models.Model):
	pass


class EmailVR(models.Model):
	code = models.CharField(max_length=20, verbose_name=u"验证码")
	email = models.EmailField(max_length=50,   null=True, verbose_name=u"邮箱")
	send_type = models.CharField(max_length=10,   null=True, choices=(("register", u"注册"), ("forget", u"未注册")))
	send_time = models.DateTimeField(default=datetime.now)

	class Meta:
		verbose_name = u"邮箱验证码"
		verbose_name_plural = verbose_name
			

	def __str__(self):
		return '{0}({1})'.format(self.code, self.email)