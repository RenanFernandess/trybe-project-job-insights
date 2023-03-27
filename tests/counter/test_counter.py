# from src.pre_built.counter import count_ocurrences
from src.pre_built.counter import count_ocurrences
import pytest
from unittest.mock import patch, mock_open


@pytest.fixture
def file():
    return """
        Analyze complex systems and troubleshoot and isolate system issues;
        Understand requirements for business users and translate into design
        specifications, utilizing thorough understanding of the Salesforce
        platform, Salesforce products and licensing models;
        Utilize thorough understanding of application development, project
        lifecycle, and methodologies and ability to work under tight deadlines
        and handle multiple detail-oriented tasks;
        Apply knowledge of Salesforce developmentand customizations, with
        APEX, Visual Force, API, Force.com and Workflows, taking into account
        com best practices, support mechanisms, procedures, and limitations,
        as well as NDR's unique needs;
        Responsible for Salesforce administration, release management and
        deployment as well as management of Salesforce.com sandboxes,
        including their integrations;
        Design and execute Salesforce.com configuration changes, leveraging
        the Salesforce interface to sync with internal tracking systems;
        Design, develop, and maintain integration and synchronization programs;
        Design the data model, user interface, business logic, and security
        for custom applications; and
        Design, develop, and customize software solutions for end users by
        using analysis and mathematical models to effectively predict and
        measure the results of the design using Chatter, Communities and other
        Salesforce applications.
        """


def test_counter(file):
    "Testa se a função count_ocurrences faz a contagem correta"

    with patch("builtins.open", mock_open(read_data=file)):
        assert count_ocurrences("fake_path", word="design") == 6
