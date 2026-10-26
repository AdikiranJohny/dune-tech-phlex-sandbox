// My first Phlex workflow: a copy of test-cpp-workflow.jsonnet to change.
// Try: a different number of spills, or fewer products in the output.
{
  driver: {
    cpp: 'generate_layers',
    layers: {
      spill: { parent: 'job', total: 10, starting_number: 1 },
    },
  },
  sources: {
    geometry_source: {
      cpp: 'geometry_source',
      geometry_name: 'standard',
    },
    numbers_source: {
      cpp: 'numbers_source',
      layer: 'spill',
    },
  },
  modules: {
    add_cpp: {
      cpp: 'add_and_verify',
      layer: 'spill',
    },
    // FORM writes these products to output.root
    output: {
      cpp: 'form_module',
      products: ['i', 'j', 'sum'],
    },
  },
}
