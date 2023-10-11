static PyObject *
getDeviceList(PyObject *self, PyObject *args)
{
	PyObject* pyList = NULL;

	HRESULT hr = CoInitializeEx(NULL, COINIT_MULTITHREADED);
	if (SUCCEEDED(hr))
	{
		IEnumMoniker *pEnum;

		hr = EnumerateDevices(CLSID_VideoInputDeviceCategory, &pEnum);
		if (SUCCEEDED(hr))
		{
			pyList = DisplayDeviceInformation(pEnum);
			pEnum->Release();
		}
		CoUninitialize();
	}

    return pyList;
}

static PyMethodDef Methods[] =
{
    {"getDeviceList", getDeviceList, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initdevice(void)
{
     (void) Py_InitModule("device", Methods);
}
