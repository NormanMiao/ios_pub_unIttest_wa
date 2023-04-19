# -*- coding: utf-8 -*-
from uitrace.api import *
import unittest

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """测试类开始执行前执行一次"""
        # 初始化设备驱动和环境
        init_driver(workspace=os.path.dirname(__file__))
        # 返回主页
        press(DeviceButton.HOME)

    @classmethod
    def tearDownClass(cls):
        """测试类结束执行后执行一次"""
        stop_driver()

    def setUp(self):
        """测试用例执行前执行一次"""
        # 启动应用：com.tencent.wetestdemo
        start_app("com.wetest.demo.db")
        time.sleep(2)

    def tearDown(self):
        """测试用例执行后执行一次"""
        # 关闭应用：com.tencent.wetestdemo
        stop_app("com.wetest.demo.db")

    def test_login_fail(self):
        """不输入账号密码，直接登录——出现Login Failed的弹窗——设置事件处理并启动——弹窗取消"""
        # 查找当前应用，并断言是否为com.wetest.demo.db
        app = current_app()
        assert app == "com.wetest.demo.db"
        # 点击SIGNIN按钮
        click(loc="//Button[@name='Sign In' and @label='Sign In']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        time.sleep(3)
        # 弹窗Login Failed
        failed_msg = find_ocr(word="Login Failed",timeout=60)
        # ocr文字识别断言内容包含Login Failed的弹窗
        assert failed_msg is not None
        print(failed_msg)
        

    def test_login_success(self):
        """输入账号密码——登录成功——进入SELECT页面——断言登录成功"""
        # 查找当前应用，并断言是否为com.wetest.demo.db
        app = current_app()
        assert app == "com.wetest.demo.db"
        # 点击“输入账号”输入框
        click(loc="//Application[1]/Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/TextField[1]", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        # 输入账号
        input_text("norman")
        #  点击“输入密码”输入框
        click(loc="//Application[1]/Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/SecureTextField[1]", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        # 输入密码
        input_text("123456")
        # 点击登录
        click(loc="//StaticText[@name='Sign In' and @label='Sign In']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        # 设置等待2s
        time.sleep(2)
        # 截图
        screenshot(label="screenshot", img_path=None, pos=None)
        # 进入SELECT页面，断言上方显示账号名
        success = find(loc="obj_1681896574997.jpg", by=DriverType.CV, timeout=30)
        assert success is not None
        print("登录成功")


    def test_check_elements(self):
        """登录——勾选item1,item10 """
        # 登录，进入SELECT页
        self.test_login_success()
        # 单击item1
        click(loc="obj_1681896768968.jpg", by=DriverType.CV, offset=None, timeout=30, duration=0.05, times=1)
        # 双击item3
        double_click(loc="obj_1681896803486.jpg", by=DriverType.CV, offset=None, timeout=30, duration=0.05)
        time.sleep(1)
        # 分别获取item7和item1的坐标，备用
        pos_from = find(loc="obj_1681896830782.jpg", by=DriverType.CV, timeout=30)
        pos_to = find(loc="obj_1681896855149.jpg", by=DriverType.CV, timeout=30)
        # 借助上面获取的坐标滑动屏幕
        slide(loc_from=pos_from, loc_to=pos_to, loc_shift=None, by=DriverType.POS, timeout=30, down_duration=0, up_duration=0, velocity=0.01)
        time.sleep(2)
        click(loc="Submit", by=DriverType.OCR)
        # 进入检查页面，检查之前选择的item1和Item10在页面上显示
        select_item =find(loc="obj_1681897094965.jpg", by=DriverType.CV, timeout=30)
        # assert select_item is not None
        # 截图
        screenshot(label="screenshot", img_path=None, pos=None)

