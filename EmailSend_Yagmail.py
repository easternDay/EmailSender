#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yagmail

# 链接邮箱服务器
username = "849919718@qq.com"
passwd = "qgazsthdfsaybedi"

mail = yagmail.SMTP(user=username,
                    password=passwd,
                    host='smtp.qq.com',  # 其他服务器就smtp.qq.com  smtp.126.com
                    smtp_ssl=True
                    )  # 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
mail.send(
    to=['849919718@qq.com', '3021921315@qq.com'],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
    cc='849919718@qq.com',  # 抄送
    subject='学习发送邮件',  # 邮件标题
    contents='你好，你今天开心吗？',  # 邮件正文
    attachments=[r'C:\Users\asus\Desktop\BK3 U1A要点总结.docx',
                 r'C:\Users\asus\Desktop\1825101045 杨祉 报告1.doc'])  # 附件如果只有一个的话，用字符串就行，attachments=r'C:\\pp\\b.txt'
print('发送成功')

