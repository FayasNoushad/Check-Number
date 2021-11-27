# Check Number
Python number checker

## Installation

```
pip install Check-Number
```

---

## Usage

```py
import check_number

print(check_number.is_number('+910000000000')
# => {"status": true}

print(check_number.is_number('Hello')
# => {"status": false}

print(check_number.is_numbers(
    ['+910000000000', '+10000000000', 'Hello']
)
# => ['+910000000000', '+10000000000']
```

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
