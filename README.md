# Human ABI

## Summary

This package provides a way to parse [Human Readable ABI](https://docs.ethers.org/v5/api/utils/abi/formats/#abi-formats--human-readable-abi) introduced by [ethers.js](https://ethers.org/) to the Python world. It's still pretty much a WIP. The goal is to be fully compatible with [ethers.js](https://ethers.org/) and [ethers-rs](https://github.com/gakonst/ethers-rs).

```bash
$ pip install human-abi
```

```py
from human_abi import HumanReadableParser

parser = HumanReadableParser('event TestEvent(uint indexed id, (string, uint16, (uint8, uint8)) value)')
print(parser.take_event())
# {'type': 'event', 'name': 'TestEvent', 'anonymous': False, 'inputs': [{'type': 'uint', 'name': 'id', 'indexed': True}, {'type': 'tuple', 'name': 'value', 'indexed': False, 'components': [{'type': 'string'}, {'type': 'uint16'}, {'type': 'tuple', 'components': [{'type': 'uint8'}, {'type': 'uint8'}]}]}]}
```

## WIP

This library is still a work-in-progress. Features are being implemented as needed. But if you find it lacks what you need, feel free to submit a pull request!

## LICENSE

Apache License 2.0