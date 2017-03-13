# import pytest so we can check for exceptions
import pytest

# import our function from where it lives
from Dev import SpringBreakChallenge

# do we have a callable function?
def test_it_is_callable():
  assert callable(SpringBreakChallenge)