# Super simple BBC microbit assertion library 

from microbit import display, Image

def micro_assert(value, message=None):
  """
  Assert that a value given is Truthy. 
  """
  if not value:
    if message is None:
      message = "Assertion failed"
      raise Exception(message)

def micro_assert_true(value, message=None):
  """
  Assert that a value given is Truthy. 
  """
  if message is None:
    message = "Expected: {}, actual: {}".format(True, value)
  micro_assert(value, message)

def micro_assert_false(value, message=None):
  """
  Assert that a value given is Falsey. 
  """
  if message is None:
    message = "Expected: {}, actual: {}".format(False, value)
  micro_assert(not value, message)

def micro_assert_equal(expected, actual, message=None):
  """
  Assert that an actual value is equal to an expected value
  """
  if message is None:
    message = "Expected: {}, actual: {}".format(expected, actual)
  micro_assert(expected == actual, message)

def micro_assert_empty(items, message=None):
  """
  Assert that a list of items is empty  
  """
  expected = 0
  actual = len(items)
  if message is None:
    message = "List expected: {} items, actual: {}".format(expected, actual)
  micro_assert(expected == actual, message)

def micro_assert_fail(message):
  """
  Force a failure without a check. 

  Example:

    ThisThingShouldHappen()
    ThisShouldThrowAnException()

    # Should not get here, ever !!!
    micro_assert_fail('this cannot be happening!!!')
    
  """
  raise Exception(message)

def micro_assert_image_equal(expected, actual):
  """
  Assert that two image objects are identical.
  Checks width and height are the same and that all
  pixel values are the same in both.
  """
    expected_width = expected.width()
    actual_width = actual.width()
    message = "Image width: expected: {}, actual: {}".format(
        expected_width, actual_width
    )
    micro_assert_equal(expected_width, actual_width, message)

    expected_height = expected.height()
    actual_height = actual.height()
    message = "Image height: expected: {}, actual: {}".format(
        expected_height, actual_height
    )
    micro_assert_equal(expected_height, actual_height, message)

    for x in range(expected_width):
        for y in range(actual_height):
            expected_pixel = expected.get_pixel(x, y)
            actual_pixel = actual.get_pixel(x, y)
            message = "Image {}, {}: expected: {}, actual: {}".format(
                x, y, expected_pixel, actual_pixel
            )
            micro_assert_equal(expected_pixel, actual_pixel, message)

def micro_assert_display_equal(expected):
  """
  Assert that the image on the display is identical to an expected Image object.
  Checks that all pixel values are the same at each x, y position. Does not check 
  width or height of expected image.
  """
    for x in range(5):
        for y in range(5):
            expected_pixel = expected.get_pixel(x, y)
            actual_pixel = display.get_pixel(x, y)
            message = "Display {}, {}: expected: {}, actual: {}".format(
                x, y, expected_pixel, actual_pixel
            )
            micro_assert_equal(expected_pixel, actual_pixel, message)
