from config_data.config import nats_settings

from nats.aio.client import Client
from nats.js import JetStreamContext
from nats.js.errors import BucketNotFoundError
from nats.js.object_store import ObjectStore

import nats


async def register_object_store() -> None:
    global object_store

    nc: Client = await nats.connect()
    js: JetStreamContext = nc.jetstream()
    
    try:
        object_store: ObjectStore = await js.object_store(nats_settings.bucket)

    except BucketNotFoundError:
        object_store: ObjectStore = await js.create_object_store(nats_settings.bucket)