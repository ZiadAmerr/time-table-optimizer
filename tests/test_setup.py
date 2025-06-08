import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd


def test_imports() -> None:
    """Test that all required libraries are properly installed and can be imported."""
    # Check that we can access version information
    assert hasattr(np, "__version__")
    assert hasattr(pd, "__version__")
    assert hasattr(nx, "__version__")
    assert hasattr(plt.matplotlib, "__version__")

    # Test random seed for reproducibility
    np.random.seed(42)
    random_numbers = np.random.rand(5)
    expected_numbers = np.array(
        [0.37454012, 0.95071431, 0.73199394, 0.59865848, 0.15601864]
    )

    # Verify that random numbers match expected values with the given seed
    np.testing.assert_allclose(random_numbers, expected_numbers)


if __name__ == "__main__":
    # This allows the file to be run directly as well
    print("Testing numpy:", np.__version__)
    print("Testing pandas:", pd.__version__)
    print("Testing networkx:", nx.__version__)
    print("Testing matplotlib:", plt.matplotlib.__version__)

    test_imports()
    print("All libraries imported successfully!")
