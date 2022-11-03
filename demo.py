# Yếu cầu
# Tạo project id và thay thế project_id phía dưới tài liệu(https://blockfrost.io/dashboard)
# cài python3
# tại folder tạo môi trường bằng cách mở terminal nhập: python -m venv venv
# tại terminal nhập: pip install blockfrost-python (blockfrost lib access node, ...)
# tại terminal python demo.py (tên file.py)
# Có thể thay thế địa chỉ thật để thấy số dư trong ví

from blockfrost import BlockFrostApi, ApiError, ApiUrls

api = BlockFrostApi(
    project_id='',  # or export environment variable BLOCKFROST_PROJECT_ID
    # optional: pass base_url or export BLOCKFROST_API_URL to use testnet, defaults to ApiUrls.mainnet.value
    base_url=ApiUrls.mainnet.value, # phụ thuộc vào khi tạo project id
)
try:
    account_rewards = api.account_rewards(
        stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
        count=20,
    )
    print(account_rewards[0].epoch)  # prints 221
    print(len(account_rewards))  # prints 20

    account_rewards = api.account_rewards(
        stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
        count=20,
        gather_pages=True, # will collect all pages
    )
    print(account_rewards[0].epoch)  # prints 221
    print(len(account_rewards))  # prints 57

    address = api.address(
        address='addr1qxqs59lphg8g6qndelq8xwqn60ag3aeyfcp33c2kdp46a09re5df3pzwwmyq946axfcejy5n4x0y99wqpgtp2gd0k09qsgy6pz')
    print(address.type)  # prints 'shelley'
    for amount in address.amount:
        print(amount.unit)  # prints 'lovelace'
        print(amount)

except ApiError as e:
    print(e)
