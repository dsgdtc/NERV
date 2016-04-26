mail=`cat /etc/libreport/plugins/abrt_mail_add/email.conf`
sed -i "/\#/b; s/EmailTo=.*/$mail/g" /etc/libreport/plugins/mailx.conf
