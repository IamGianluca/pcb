import pcb.domain.model as model
from pcb.domain.model import MIN_WIDTH


def test_bus_rule_assignement():
    a0 = model.Net("a0")
    a1 = model.Net("a1")
    a = model.Bus("a")

    a.add_net(a0)
    a.add_net(a1)

    min_width_4 = model.NetRule.create_rule(MIN_WIDTH, 4)
    a.assign_rule(min_width_4)

    assert min_width_4 in a0.assigned_rules()
    assert a0.get_rule(MIN_WIDTH) == min_width_4
    assert a1.get_rule(MIN_WIDTH) == min_width_4
