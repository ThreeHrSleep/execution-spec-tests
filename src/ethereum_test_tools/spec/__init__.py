"""
Test spec definitions and utilities.
"""

from typing import List, Type

from .base.base_test import BaseFixture, BaseTest, TestSpec
from .blockchain.blockchain_test import BlockchainTest, BlockchainTestFiller, BlockchainTestSpec
from .eof.eof_test import EOFTest, EOFTestFiller, EOFTestSpec
from .fixture_collector import FixtureCollector, TestInfo
from .state.state_test import StateTest, StateTestFiller, StateTestOnly, StateTestSpec

SPEC_TYPES: List[Type[BaseTest]] = [BlockchainTest, StateTest, StateTestOnly, EOFTest]

__all__ = (
    "SPEC_TYPES",
    "BaseFixture",
    "BaseTest",
    "BlockchainTest",
    "BlockchainTestFiller",
    "BlockchainTestSpec",
    "EOFTest",
    "EOFTestFiller",
    "EOFTestSpec",
    "FixtureCollector",
    "StateTest",
    "StateTestFiller",
    "StateTestOnly",
    "StateTestSpec",
    "TestInfo",
    "TestSpec",
)
