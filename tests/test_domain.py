import pcb.domain.model as model
from pcb.domain.model import NetRule


def test_bus_rule_assignement():
    a0 = model.Net("a0")
    a1 = model.Net("a1")
    a = model.Bus("a")

    a.add_net(a0)
    a.add_net(a1)

    rule_type = "MIN_WIDTH"
    min_width_4 = model.NetRule.create_rule(rule_type, 4)
    a.assign_rule(min_width_4)

    assert min_width_4 in a0.assigned_rules()
    assert a0.get_rule(rule_type) == min_width_4
    assert a1.get_rule(rule_type) == min_width_4


def test_soemthing():
    # given
    bus_name, rule_type, parameter = "a", "a_rule_type", 16
    bus = model.Bus(bus_name)

    a0 = model.Net("a0")
    a1 = model.Net("a1")
    bus.add_net(a0)
    bus.add_net(a1)

    model.BusRepository.add(bus)

    # when
    model.assign_bus_rule(bus_name, rule_type, parameter)

    # then
    assert a0.get_rule(rule_type) == NetRule(rule_type, parameter)
    assert a1.get_rule(rule_type) == NetRule(rule_type, parameter)
