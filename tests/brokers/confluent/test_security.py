import ssl
from contextlib import contextmanager
from typing import Tuple
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from docs.docs_src.confluent.security.ssl_warning import test_without_ssl_warning

__all__ = ["test_without_ssl_warning"]


@contextmanager
def patch_aio_consumer_and_producer() -> Tuple[MagicMock, MagicMock]:
    try:
        consumer = MagicMock(return_value=AsyncMock())
        producer = MagicMock(return_value=AsyncMock())

        # with patch("faststream.confluent.client.Consumer", new=consumer), patch(
        #     "faststream.confluent.client.Producer", new=producer
        # ):
        #     yield consumer, producer
        with patch(
            "faststream.confluent.broker.AsyncConfluentConsumer", new=consumer
        ), patch("faststream.confluent.broker.AsyncConfluentProducer", new=producer):
            yield consumer, producer
    finally:
        pass


@pytest.mark.asyncio()
@pytest.mark.confluent()
async def test_base_security():
    with patch_aio_consumer_and_producer() as (consumer, producer):
        from docs.docs_src.confluent.security.basic import broker as basic_broker

        @basic_broker.subscriber("test")
        async def handler():
            ...

        async with basic_broker:
            await basic_broker.start()

        consumer_call_kwargs = consumer.call_args.kwargs
        producer_call_kwargs = producer.call_args.kwargs

        call_kwargs = {}
        call_kwargs["security_protocol"] = "SSL"

        assert call_kwargs.items() <= consumer_call_kwargs.items()
        assert call_kwargs.items() <= producer_call_kwargs.items()

        assert (
            consumer_call_kwargs["security_protocol"]
            == call_kwargs["security_protocol"]
        )
        assert (
            producer_call_kwargs["security_protocol"]
            == call_kwargs["security_protocol"]
        )

        assert type(consumer_call_kwargs["ssl_context"]) == ssl.SSLContext
        assert type(producer_call_kwargs["ssl_context"]) == ssl.SSLContext


@pytest.mark.asyncio()
@pytest.mark.confluent()
async def test_scram256():
    with patch_aio_consumer_and_producer() as (consumer, producer):
        from docs.docs_src.confluent.security.sasl_scram256 import (
            broker as scram256_broker,
        )

        @scram256_broker.subscriber("test")
        async def handler():
            ...

        async with scram256_broker:
            await scram256_broker.start()

        consumer_call_kwargs = consumer.call_args.kwargs
        producer_call_kwargs = producer.call_args.kwargs

        call_kwargs = {}
        call_kwargs["sasl_mechanism"] = "SCRAM-SHA-256"
        call_kwargs["sasl_plain_username"] = "admin"
        call_kwargs["sasl_plain_password"] = "password"  # pragma: allowlist secret
        call_kwargs["security_protocol"] = "SASL_SSL"

        assert call_kwargs.items() <= consumer_call_kwargs.items()
        assert call_kwargs.items() <= producer_call_kwargs.items()

        assert (
            consumer_call_kwargs["security_protocol"]
            == call_kwargs["security_protocol"]
        )
        assert (
            producer_call_kwargs["security_protocol"]
            == call_kwargs["security_protocol"]
        )

        assert type(consumer_call_kwargs["ssl_context"]) == ssl.SSLContext
        assert type(producer_call_kwargs["ssl_context"]) == ssl.SSLContext


@pytest.mark.asyncio()
@pytest.mark.confluent()
async def test_scram512():
    with patch_aio_consumer_and_producer() as (consumer, producer):
        from docs.docs_src.confluent.security.sasl_scram512 import (
            broker as scram512_broker,
        )

        @scram512_broker.subscriber("test")
        async def handler():
            ...

        async with scram512_broker:
            await scram512_broker.start()

        consumer_call_kwargs = consumer.call_args.kwargs
        producer_call_kwargs = producer.call_args.kwargs

        call_kwargs = {}
        call_kwargs["sasl_mechanism"] = "SCRAM-SHA-512"
        call_kwargs["sasl_plain_username"] = "admin"
        call_kwargs["sasl_plain_password"] = "password"  # pragma: allowlist secret
        call_kwargs["security_protocol"] = "SASL_SSL"

        assert call_kwargs.items() <= consumer_call_kwargs.items()
        assert call_kwargs.items() <= producer_call_kwargs.items()

        assert (
            consumer_call_kwargs["security_protocol"]
            == call_kwargs["security_protocol"]
        )
        assert (
            producer_call_kwargs["security_protocol"]
            == call_kwargs["security_protocol"]
        )

        assert type(consumer_call_kwargs["ssl_context"]) == ssl.SSLContext
        assert type(producer_call_kwargs["ssl_context"]) == ssl.SSLContext


@pytest.mark.asyncio()
@pytest.mark.confluent()
async def test_plaintext():
    with patch_aio_consumer_and_producer() as (consumer, producer):
        from docs.docs_src.confluent.security.plaintext import (
            broker as plaintext_broker,
        )

        @plaintext_broker.subscriber("test")
        async def handler():
            ...

        async with plaintext_broker:
            await plaintext_broker.start()

        consumer_call_kwargs = consumer.call_args.kwargs
        producer_call_kwargs = producer.call_args.kwargs

        call_kwargs = {}
        call_kwargs["sasl_mechanism"] = "PLAIN"
        call_kwargs["sasl_plain_username"] = "admin"
        call_kwargs["sasl_plain_password"] = "password"  # pragma: allowlist secret
        call_kwargs["security_protocol"] = "SASL_SSL"

        assert call_kwargs.items() <= consumer_call_kwargs.items()
        assert call_kwargs.items() <= producer_call_kwargs.items()

        assert (
            consumer_call_kwargs["security_protocol"]
            == call_kwargs["security_protocol"]
        )
        assert (
            producer_call_kwargs["security_protocol"]
            == call_kwargs["security_protocol"]
        )

        assert type(consumer_call_kwargs["ssl_context"]) == ssl.SSLContext
        assert type(producer_call_kwargs["ssl_context"]) == ssl.SSLContext
