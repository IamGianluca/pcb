from enum import Enum
from typing import List, Optional


class NetRule:
    def __init__(self, rule, number) -> None:
        self.rule = rule
        self.number = number

    @staticmethod
    def create_rule(rule: Enum, number: int):
        return NetRule(rule, number)


class Net:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rules: List[NetRule] = []

    def assign_rule(self, rule: NetRule) -> None:
        self.rules.append(rule)

    def assigned_rules(self) -> List[NetRule]:
        return self.rules

    def get_rule(self, a_rule: Enum) -> NetRule:
        return [r for r in self.rules if r.rule == a_rule][0]


class Bus:
    def __init__(self, name: str) -> None:
        self.name = name
        self.nets: List = []

    def add_net(self, net: Net):
        self.nets.append(net)

    def assign_rule(self, rule: NetRule):
        for net in self.nets:
            net.assign_rule(rule)


class MIN_WIDTH(Enum):
    pass
