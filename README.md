# simple-microbit-assert
Simplest BBC microbit assertion library

## Example:

```python

from microbit import *
from micro-assert import *

micro_assert(1 == 2, "Maths!")

display.show(Image("99999:99999:99999:99999:99999"))
micro_assert_display_equal(Image("00000:00000:00000:00000:00000"))

```
