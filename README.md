本示例用unittest组织测试用例，完成对wetestdemo的测试，包括登录失败、登录成功、检查勾选内容三个场景。

【用例介绍】

测试用例1: 登录失败场景

不输入账号密码，直接登录，出现Login Failed的提示，断言该提示出现。

测试用例2: 登录成功场景

输入账号密码，登录成功。进入SELECT页面，查找页面元素并断言。

测试用例3: 检查勾选内容

登录成功后，SELECT页面选中item1，然后进入检查页面，检查之前选择的item1在页面上显示。

【被测应用及框架】

被测系统：安卓

被测应用:WeTest_Demo_enterprise.ipa

自动化框架：Weautomator
