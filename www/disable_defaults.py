from browser import document

kc = dict(
	F5=116,
	F4=115,
	F3=114,
	F2=113,
	F1=112,
	O=79,
	T=84,
	W=87,
	N=78,
	R=82,
	S=83
)


def disable_defaults(ev):
	_filter = [
		kc['F1'],
		kc['F2'],
		kc['F3'],
		kc['F4'],
		kc['F5']
	]

	ctrl_filter = [
		kc['O'], kc['T'], kc['W'], kc['N'], kc['R'], kc['S']
	]

	if ev.keyCode in _filter or (ev.keyCode in ctrl_filter and ev.ctrlKey):
		ev.preventDefault()



document.bind('keydown', disable_defaults)