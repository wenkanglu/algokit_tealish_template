from base64 import b64decode
from os import path

from algokit_utils import Account
from algosdk.atomic_transaction_composer import (
    AtomicTransactionComposer,
    TransactionWithSigner,
)
from algosdk.logic import get_application_address
from algosdk.transaction import (
    ApplicationCreateTxn,
    OnComplete,
    StateSchema,
)
from algosdk.v2client.algod import AlgodClient

BUILD_PATH_PREFIX = path.join(path.dirname(__file__), "../contracts/build/")


def deploy_app(
    deployer_account: Account,
    approval_name: str,
    clear_name: str,
    client: AlgodClient,
    global_schema: StateSchema = StateSchema(num_uints=0, num_byte_slices=0),
    local_schema: StateSchema = StateSchema(num_uints=0, num_byte_slices=0),
) -> tuple[int, str]:
    with open(BUILD_PATH_PREFIX + approval_name, "r") as approval:
        with open(BUILD_PATH_PREFIX + clear_name, "r") as clear:
            atc = AtomicTransactionComposer()
            atc.add_transaction(
                TransactionWithSigner(
                    txn=ApplicationCreateTxn(
                        sender=deployer_account.address,
                        sp=client.suggested_params(),
                        on_complete=OnComplete.NoOpOC.real,
                        approval_program=_compile_program(approval.read(), client),
                        clear_program=_compile_program(clear.read(), client),
                        global_schema=global_schema,
                        local_schema=local_schema,
                    ),
                    signer=deployer_account.signer,
                )
            )
            tx_id = atc.execute(client, 5).tx_ids[0]
            tx_info = client.pending_transaction_info(tx_id)
            app_id = tx_info["application-index"]
            logs = tx_info["logs"]
            app_address = get_application_address(app_id)

            return app_id, app_address, logs


def _compile_program(source_code: str, client: AlgodClient) -> bytes:
    compile_response = client.compile(source_code)
    return b64decode(compile_response["result"])
