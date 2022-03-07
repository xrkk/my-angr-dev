import os
import angr

test_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'binaries', 'tests')


def test_vtable_extraction_x86_64():
    p = angr.Project(os.path.join(test_location, "x86_64", "cpp_classes"), auto_load_libs=False)
    vtables_sizes = {0x403cb0: 24, 0x403cd8: 16, 0x403cf8: 16, 0x403d18: 16}
    vtable_analysis = p.analyses.VtableFinder()
    vtables = vtable_analysis.vtables_list

    assert len(vtables) == 4

    for vtable in vtables:
        assert vtable.vaddr in [0x403cb0, 0x403cd8, 0x403cf8, 0x403d18]
        assert vtables_sizes[vtable.vaddr] == vtable.size


if __name__ == "__main__":
    test_vtable_extraction_x86_64()
