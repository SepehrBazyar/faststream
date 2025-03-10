import pytest

from faststream import context
from tests.marks import python39


@pytest.mark.asyncio()
@python39
async def test_kafka():
    from docs.docs_src.getting_started.context.kafka.initial import broker
    from faststream.kafka import TestKafkaBroker

    async with TestKafkaBroker(broker) as br:
        await br.publish("", "test-topic")
        await br.publish("", "test-topic")

    assert context.get("collector") == ["", ""]
    context.clear()


@pytest.mark.asyncio()
@python39
async def test_rabbit():
    from docs.docs_src.getting_started.context.rabbit.initial import broker
    from faststream.rabbit import TestRabbitBroker

    async with TestRabbitBroker(broker) as br:
        await br.publish("", "test-queue")
        await br.publish("", "test-queue")

    assert context.get("collector") == ["", ""]
    context.clear()


@pytest.mark.asyncio()
@python39
async def test_nats():
    from docs.docs_src.getting_started.context.nats.initial import broker
    from faststream.nats import TestNatsBroker

    async with TestNatsBroker(broker) as br:
        await br.publish("", "test-subject")
        await br.publish("", "test-subject")

    assert context.get("collector") == ["", ""]
    context.clear()


@pytest.mark.asyncio()
@python39
async def test_redis():
    from docs.docs_src.getting_started.context.redis.initial import broker
    from faststream.redis import TestRedisBroker

    async with TestRedisBroker(broker) as br:
        await br.publish("", "test-channel")
        await br.publish("", "test-channel")

    assert context.get("collector") == ["", ""]
    context.clear()
