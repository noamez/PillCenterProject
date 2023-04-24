@echo off

echo.
echo Cloning GIT repositories...
git clone --quiet --single-branch --branch 51-build-for-production git@gitlab.com:pillcenter-dev/%PROJECT_NAME%.git
echo.
echo Cleaning up development code from server...
pushd %PROJECT_NAME%
rd ".git" /S /Q
popd

exit /B 1
