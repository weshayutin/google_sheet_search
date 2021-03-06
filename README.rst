Taken from: https://developers.google.com/sheets/api/quickstart/python

To run gs_search.py, you'll need:
====================================

* Python 2.6 or greater.
* The pip package management tool.
* A Google account.

Credentials
-----------

* Step 1: Turn on the Google Sheets API
* Use this wizard [1]  to create or select a project in the Google Developers Console and automatically turn on the API.
* Click Continue, then Go to credentials.
* On the Add credentials to your project page, click the Cancel button.
* At the top of the page, select the OAuth consent screen tab.
   * Select an Email address,
   * enter a Product name if not already set,
   * and click the Save button.
* Select the Credentials tab,
   * click the Create credentials button
   * and select OAuth client ID.
* Select the application type Other,
   * enter the name "Google Sheets API Quickstart",
   * and click the Create button.
* Click OK to dismiss the resulting dialog.
* Click the file_download (Download JSON) button to the right of the client ID.

* Move this file to your working directory and rename it client_secret.json.
* Result: you should have two files:
   * client_secret.json
   * credentials.json

Pip install
-----------

* Step 2: Install the Google Client Library
   * Run the following command to install the library using pip::

      pip install --upgrade google-api-python-client

Example
-------

* Example invocation::

   chmod +x gs_search.py
   ./gs_search.py -s Hyper

* Results::

    |                 TripleO Service                   |                      Default                       |        puppet/services/        |        docker/service/         |              DFG              |
    ___________________________________________________________________________________________________________________________________________________________________________________________________________


    |OS::TripleO::Services::CinderBackendVRTSHyperScale |                   OS::Heat::None                   | cinder-backend-veritas-hypersc |                                |            Storage            |
    |OS::TripleO::Services::CinderBackendVRTSHyperScale |                   OS::Heat::None                   | cinder-backend-veritas-hypersc |                                |            Storage            |
    |      OS::TripleO::Services::VRTSHyperScale        |                   OS::Heat::None                   | veritas-hyperscale-controller. |                                |            Storage            |
    |      OS::TripleO::Services::VRTSHyperScale        |                   OS::Heat::None                   | veritas-hyperscale-controller. |                                |            Storage            |
