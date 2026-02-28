# rudder-tools
The toolset to operate with Normation "Rudder"

It implements object replication between two (or more) rudder servers, realising a kind of "one to many" relation.

The replication model is rule-based.
You should design your rules so that one directive applies to only one rule.
Rule is replicated together with it's rule tree's branch.

There is no way to implement exactly fair transaction model.
But, I sought to approach to transaction model as close as it ever could be done.

Groups are also replicated together with their rule tree's branches, by means of "rudder_groups" tool.

### Links:
[Vendor's website](https://www.rudder.io/)

[WIKI](https://en.wikipedia.org/wiki/Rudder_(software))

[Rudder API reference](https://docs.rudder.io/api/v/21/)
