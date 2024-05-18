from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_whatsapp_intigration/__init__.py
from erp_whatsapp_intigration import __version__ as version

setup(
	name="erp_whatsapp_intigration",
	version=version,
	description="WhatsAPP",
	author="caratred",
	author_email="infor@caratred.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
