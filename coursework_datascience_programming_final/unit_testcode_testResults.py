import matplotlib.pyplot as plt
from matplotlib.animation import anim
import numpy as np

from controller.testResults import visualize_test_scores

def test_visualize_test_scores():
    # Test data
    test_scores = [
        {'Table': 'Mock_Test', 'Grade': 90},
        {'Table': 'Formative_Test_1', 'Grade': 85},
        {'Table': 'Formative_Test_2', 'Grade': 95},
        {'Table': 'Formative_Test_3', 'Grade': 88},
        {'Table': 'Formative_Test_4', 'Grade': 92},
        {'Table': 'SumTest', 'Grade': 80}
    ]
    student_id = 123

    # Call the function
    anim = visualize_test_scores(test_scores, student_id)

    # Assertions
    assert isinstance(anim, plt.animation.FuncAnimation)
    assert anim.event_source.interval == 50
    assert anim.event_source.frames == 100

    # Check the plot
    fig = plt.gcf()
    ax = plt.gca()
    assert ax.get_title() == f'Test Scores for Student {student_id}'
    assert ax.get_xlabel() == 'Table'
    assert ax.get_ylabel() == 'Grade'
    assert ax.get_ylim() == (0, 110)

    bars = ax.containers[0]
    assert len(bars) == len(test_scores)

    for i, bar in enumerate(bars):
        assert bar.get_height() == test_scores[i]['Grade'] * (i + 1) / 100

    plt.close(fig)

# Call the test function
test_visualize_test_scores()
