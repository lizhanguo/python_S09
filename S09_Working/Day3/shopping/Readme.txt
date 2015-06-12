Hi,

本系统模拟了信用卡网上购物，ATM机取现、还款等功能。

使用方法如下：
(1)确保操作系统为Linux，使用python 2.7 及以上版本（python 3.0 除外）；
(2)确保atm.py , login.py , record_type.py , shopping.py , account.pkl , goods.pkl , credit.log , lock.txt pickle_run.py 这些文件在统一目录下；
(3)运行主程序：python atm.py 
(4)按终端屏幕提示输入用户名或密码！按提示操作!

说明：
pickle_run.py   用于提前生成 account.pkl 和 goods.pkl 文件 
atm.py          程序主文件，直接运行
login.py        用户登陆认证功能模块
record_type.py  取现、还款、转账、购物等消费类型功能模块
shopping.py     网上购物功能模块
account.pkl     用户信息文件
lock.txt        锁定用户信息文件 
goods.pkl       商品信息文件
credit.log      消费信息记录日志


