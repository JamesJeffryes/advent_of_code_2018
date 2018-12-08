
def parse_subtree_sum(flat_tree, pointer):
    n_children = flat_tree[pointer]
    n_metadata = flat_tree[pointer + 1]
    children = []
    metadata_sum = 0
    pointer += 2
    while len(children) < n_children:
        child, child_meta_sum, pointer = parse_subtree_sum(flat_tree, pointer)
        children.append(child)
        metadata_sum += child_meta_sum

    metadata = flat_tree[pointer:pointer + n_metadata]
    metadata_sum += sum(metadata)
    pointer += n_metadata

    return (children, metadata), metadata_sum, pointer


def parse_subtree_value(flat_tree, pointer):
    n_children = flat_tree[pointer]
    n_metadata = flat_tree[pointer + 1]
    children = []
    value = 0
    pointer += 2
    while len(children) < n_children:
        child_value, pointer = parse_subtree_value(flat_tree, pointer)
        children.append(child_value)

    metadata = flat_tree[pointer:pointer + n_metadata]
    if not n_children:
        value += sum(metadata)
    else:
        value = sum((children[x-1] for x in metadata if x <= len(children)))

    pointer += n_metadata

    return value, pointer


with open('inputs/08.txt') as infile:
    input_list = [int(x) for x in infile.read().split()]
    tree, metadata_sum, _ = parse_subtree_sum(input_list, 0)
    print(metadata_sum)
    value, _ = parse_subtree_value(input_list, 0)
    print(value)

