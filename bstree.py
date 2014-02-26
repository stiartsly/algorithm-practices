import sys

## {"parent": None,
#   "value" : xx,
#   "left"  : xx,
#   "right" : xx }

def visitInorder(root, visitor):
    if root is None:
        return 
    if root["left"] is not None:
        visitInorder(root["left" ], visitor)
    visitor(root["value"])
    if root["right"] is not None:
        visitInorder(root["right"], visitor)

def _makeNode(value):
    return {"left" : None, "right": None, "value": value}

def insertValue(root, value):
    parent = None
    cur    = root

    while cur is not None:
        parent = cur
        if value <= cur["value"]:
            cur = cur["left"]
        else:
            cur = cur["right"] 

    ins = _makeNode(value)
    if parent is None:
        root = cur = ins
    elif value <= parent["value"]:
        parent["left"] = ins 
    else :
        parent["right"] = ins
    ins["parent"] = parent
    return root

def _transplant(root, u, v):
    if u["parent"] is None:
        root = v
    elif u == u["parent"]["left"]:
        u["parent"]["left"] = v
    else:
        u["parent"]["right"] = v

    if v is not None:
        v["parent"]  = u["parent"]
    return root

def _minimum_node(node):
    cur = node
    while cur["left"] is not None:
        cur = cur["left"]
    return cur
        
def _deleteNode(root, node):
    if node["left"] is None:
        root = _transplant(root, node, node["right"])
    elif node["right"] is None:
        root = _transplant(root, node, node["left"])
    else:
        minNode = _minimum_node(node["right"])
        if minNode["parent"] != node:
            root = _transplant(root, minNode, minNode["right"])
            minNode["right"] = node["right"]
            minNode["right"]["parent"] = minNode
        root = _transplant(root, node, minNode)
        minNode["left"] = node["left"]
        minNode["left"]["parent"] = minNode
    return root

def deleteValue(root, value):
    parent = None
    cur    = root

    while cur is not None:
        if value == cur["value"]:
            break
        parent = cur
        if value < cur["value"]:
            cur = cur["left"]
        else:
            cur = cur["right"]

    if cur is None:
        return None
    else:
        return _deleteNode(root, cur)
    
#--------------------------------
if __name__ == "__main__":
    def printValue(value):
        sys.stdout.write(str(value) + " ")

    a = [892,10, 23, 56, 78, 89, 3, 80, 23, 45, 100, 4, 13, 0] 
    print "original array: ", a
    root = None
    for item in a:
        root = insertValue(root, item)
        sys.stdout.write("after ins %3d: "%item)
        visitInorder(root, printValue)
        sys.stdout.write("\n")

    sys.stdout.write("---\n")
    for item in a:
        root = deleteValue(root, item)
        sys.stdout.write("after del %3d: "%item)
        visitInorder(root, printValue)
        sys.stdout.write("\n")
