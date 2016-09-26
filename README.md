# S4A
This a test project for Smart4Aviation

environment:
This project supports only Python 3.x version (3.5).

To setup your environment you should:
* Download and install python 3.5 - https://www.python.org/downloads/
* Add installed python to your system environment - https://sites.google.com/a/chromium.org/chromedriver/downloads
* Install all required python libraries: selenium, faker, nose, fake-factory, nose-htmloutput.
    ** The main directory of the test project contains requirements.txt file. If you want install all required python libraries, type in commnad line: pip3 install -r requirements.txt
* Download and add to system environment chromedriver or other browser driver you want to use for testing - project supports all browsers (tested only Firefox and Chrome)

If you correctly setup your test environment, test suite should be ready to launch:
* Open command line and navigate to path/to/test/directroy
* Now type command: nosetests --with-html --nocapture --nologcapture --with-xunit

TEST RESULTS:
Nosetests framework generates simple html test report. Test report file 'nosetests.html' is stored in main directory.
Besides it is also generated nosetests.xml file which can be used for test reporting by Jenkins or any other CI tool (read more about Jenkins test report analyzer plugin here: https://wiki.jenkins-ci.org/display/JENKINS/Test+Results+Analyzer+Plugin )
If any test cases failed, script automatically capture the screenshot and save as png file in S4A/screenshots/test_name.png. _