










import os
import sys
import traceback
from getpass import getpass
from pprint import pprint
from django.core import management

from django.contrib.auth.models import User, UserManager
from django.core.management import BaseCommand
from django.core.management.base import OutputWrapper, CommandError

from app.app_models.config_model import Config
from app.app_models.content_model import Article, Category, Tag, ArticleMeta, ArticleCategory, ArticleTag, Comment
from app.manager.config_manager import cache_config
from app.manager.ct_manager import update_one_to_many_relation_model
from tool.datetime_helper import str_to_datetime, now

"""


2020年7月02日 19:43:33
['新号回归，再相逢。 ']
"""

class Command(BaseCommand):
    """
    初始化

    python manage.py init_deeru

    """
    def handle(self, *args, **options):
        #all_data = Article.objects.all()
        #print(all_data)

        import requests

        import re
        from lxml import etree
        import lxml

        for page_num in range(1, 100):
            url = "http://guyeshanren2011.com/weibo/%E5%B1%B1%E4%BA%BA2011theone?page=" + str(page_num)
            # 你需要爬取的网页
            html = requests.get(url)
            html.encoding = "utf-8"
            selecter = etree.HTML(html.text)

            for i in range(1, 100):
                # selecter = etree.HTML(html.text)
                # print(selecter)
                rule2 = "/html/body/div/div[" + str(i) + "]/p/text()"
                rule3 = "/html/body/div/a[" + str(i) + "]/h4/text()"

                # print(rule2,rule3)
                date_info = selecter.xpath(rule3)
                # print(date_info)
                mat = re.search(r"(\d{4}年\d{1,2}月\d{1,2}日\s\d{1,2}:\d{1,2}:\d{1,2})", str(date_info))
                if mat:
                    time_get = (mat.group())

                    sstring = selecter.xpath(rule2)
                    print(sstring)

                    title_a = sstring[0]
                    title = title_a[0:250] if len(title_a) > 250 else title_a
                    title_sample = title_a[0:20] if len(title_a) > 20 else title

                    if len(sstring) >= 2:

                        body = str(time_get)+"#"+str(sstring[1])

                    else:
                        body = str(time_get)+"#"+str(sstring[0])

                    print(title, body)

                    if Article.objects.filter(title__icontains=title_sample).exists():
                        pass
                    else:
                        try:

                            summary = body[0:50] if len(body)>100 else body

                            a = Article.objects.create(
                                title = title,
                                summary = summary,
                                content = body,

                            )
                            num = a.id
                            b = ArticleMeta.objects.update_or_create(
                                article_id = num,
                                defaults={
                                    'read_num': 0,
                                    'comment_num': 0,
                                }
                            )
                            # c = ArticleCategory.objects.create(
                            #     article_id = num,
                            #     category_id = 5,
                            # )
                        except Exception as e:
                            print(e)
                            pass
                    print('success')

        return

    def handle2(self, *args, **options):
        self.error = self.stderr.write

        info_out = OutputWrapper(sys.stdout)
        info_out.style_func = self.style.WARNING
        self.info = info_out.write

        success_out = OutputWrapper(sys.stdout)
        success_out.style_func = self.style.SUCCESS
        self.success = success_out.write

        self.info("初始化中：")
        try:
            os.mkdir('log')
        except:
            pass
        with open('./log/init.log', 'a', encoding='utf-8')as f:
            f.write('开始初始化(%s)\n' % str(now()))

        # ============

        self.info('同步数据库修改 ... ')

        with open('./log/init.log', 'a', encoding='utf-8')as f:
            f.write('同步数据库修改\n')
            try:
                management.call_command('migrate', stdout=f)
            except:

                traceback.print_exc(file=f)
                self.error('同步数据库修改 ... [失败]，更多信息查看 ./log/init.log ')
                raise

        self.success('同步数据库修改 ... [完成]')

        # ============

        self.info('初始化静态文件 ... ')
        with open('./log/init.log', 'a', encoding='utf-8')as f:
            f.write('初始化静态文件\n')
            try:
                management.call_command('collectstatic', '-c', '--noinput', stdout=f)
            except:
                traceback.print_exc(file=f)
                self.error('初始化静态文件 ... [失败]，更多信息查看 ./log/init.log ')
                raise

        self.success('初始化静态文件 ... [完成]')

        # ============

        self.info('创建管理员账户 ... ')
        is_create_user = 'y'
        if User.objects.count() > 0:
            is_create_user = input('已存在管理员账户，是否创建新的管理员（ y/n，默认：n ）')
            if not is_create_user:
                is_create_user = 'n'

        if is_create_user == 'y':
            username = input('输入管理账户登录名（默认：admin）：')
            if not username:
                username = 'admin'
            password = getpass('输入密码（默认：123456）：')
            if not password:
                password = '123456'
            with open('./log/init.log', 'a', encoding='utf-8')as f:
                try:
                    flag = True
                    User._default_manager.db_manager('default').create_superuser(username, None, password)
                    self.success('创建管理员账户 ... [完成]')
                except:
                    flag = False
                    traceback.print_exc(3)

                    traceback.print_exc(file=f)
                    self.error('创建管理员账户 ... [失败]，更多信息查看 ./log/init.log ')


                finally:
                    if not flag:
                        return
        else:
            self.info('跳过创建管理员')

        self.success('\n初始化完成 ！！')


