import requests
from core.config import settings
from core.logger_info import logger

def get_proxy():
    try:
        proxy = requests.get(settings.S5PROXY_URL).text
        host, port = proxy.split(':')
        data = {"proxy_type": "socks5", "proxy_host": host,
                "proxy_port": port.strip(), "proxy_user": "ExemplWinke@gmail.com",
                "proxy_password": "Qwe123321..", "proxy_soft": "other"}
        logger.info(f"成功获取s5代理")
        return data
    except Exception as e:
        logger.error(f"获取代理失败：{str(e)}")


def get_proxy_guys():
    """
209.248.72.241:8083
    :return:
    """
    data = {"proxy_type": "socks5", "proxy_host": "209.248.72.241",
            "proxy_port": "9093", "proxy_user": "pg_bgadkbc2.custom1",
            "proxy_password": "45201981fa", "proxy_soft": "other"}
    logger.info(f"成功获取guys代理")
    return data


if __name__ == '__main__':
    result = get_proxy()
    print(result)
