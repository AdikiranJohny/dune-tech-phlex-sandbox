#include "phlex/module.hpp"

#include <cassert>

namespace {
  // Multiply the two numbers from the source
  int multiply(int i, int j) { return i * j; }
}

PHLEX_REGISTER_ALGORITHMS(m, config)
{
  using namespace phlex;

  auto const layer = config.get<std::string>("layer");

  m.transform("multiply", multiply, concurrency::unlimited)
    .input_family(product_selector{.creator = "input", .layer = layer, .suffix = "i"},
                  product_selector{.creator = "input", .layer = layer, .suffix = "j"})
    .output_product_suffixes("product");

  // numbers_source gives j = -i, so the product is -i*i and can never be positive
  m.observe(
     "verify_product", [](int product) { assert(product <= 0); }, concurrency::unlimited)
    .input_family(product_selector{.creator = "multiply", .layer = layer});
}
