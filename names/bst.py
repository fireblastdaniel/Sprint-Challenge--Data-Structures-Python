class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = TreeNode(value)
    else:
      if self.left:
        self.left.insert(value)
      else:
        self.left = TreeNode(value)

  def contains(self, target):
    current_node = self
    while current_node.value != target:
      if current_node.value > target:
        if current_node.left:
          current_node = current_node.left
        else:
          return False
      else:
        if current_node.right:
          current_node = current_node.right
        else:
          return False
    return True