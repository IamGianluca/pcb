from typing import List


class NetRule:
    def __init__(self, rule: str, number: int) -> None:
        self.rule = rule
        self.number = number

    @staticmethod
    def create_rule(rule_type: str, parameter: int):
        return NetRule(rule_type, parameter)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, NetRule):
            raise ValueError()
        return self.rule == o.rule and self.number == o.number


class Net:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rules: List[NetRule] = []

    def assign_rule(self, rule: NetRule) -> None:
        self.rules.append(rule)

    def assigned_rules(self) -> List[NetRule]:
        return self.rules

    def get_rule(self, a_rule: str) -> NetRule:
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


class BusRepository:
    buses: List = []

    @classmethod
    def add(cls, bus: Bus) -> None:
        cls.buses.append(bus)

    @classmethod
    def get_by_name(cls, bus_name: str) -> Bus:
        return [b for b in cls.buses if b.name == bus_name][0]


def assign_bus_rule(bus_name: str, rule_type: str, parameter: int) -> None:
    bus = BusRepository.get_by_name(bus_name)
    bus.assign_rule(NetRule(rule_type, parameter))
