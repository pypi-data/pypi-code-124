# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from typing import List

from libcst.codegen.gather import imports, nodebases, nodeuses

generated_code: List[str] = []
generated_code.append("# Copyright (c) Meta Platforms, Inc. and affiliates.")
generated_code.append("#")
generated_code.append(
    "# This source code is licensed under the MIT license found in the"
)
generated_code.append("# LICENSE file in the root directory of this source tree.")
generated_code.append("")
generated_code.append("")
generated_code.append("# This file was generated by libcst.codegen.gen_type_mapping")
generated_code.append("from typing import Dict as TypingDict, Type, Union")
generated_code.append("")
generated_code.append("from libcst._maybe_sentinel import MaybeSentinel")
generated_code.append("from libcst._removal_sentinel import RemovalSentinel")
generated_code.append("from libcst._nodes.base import CSTNode")

# Import the types we use. These have to be type guarded since it would
# cause an import cycle otherwise.
generated_code.append("")
generated_code.append("")
for module, objects in imports.items():
    generated_code.append(f"from {module} import (")
    generated_code.append(f"    {', '.join(sorted(list(objects)))}")
    generated_code.append(")")

# Generate the base visit_ methods
generated_code.append("")
generated_code.append("")
generated_code.append(
    "TYPED_FUNCTION_RETURN_MAPPING: TypingDict[Type[CSTNode], object] = {"
)
for node in sorted(nodebases.keys(), key=lambda node: node.__name__):
    name = node.__name__
    if name.startswith("Base"):
        continue
    valid_return_types: List[str] = [nodebases[node].__name__]
    node_uses = nodeuses[node]
    base_uses = nodeuses[nodebases[node]]
    if node_uses.maybe or base_uses.maybe:
        valid_return_types.append("MaybeSentinel")
    if (
        node_uses.optional
        or node_uses.sequence
        or base_uses.optional
        or base_uses.sequence
    ):
        valid_return_types.append("RemovalSentinel")
    generated_code.append(f'    {name}: Union[{", ".join(valid_return_types)}],')
generated_code.append("}")

if __name__ == "__main__":
    # Output the code
    print("\n".join(generated_code))
