from setuptools import setup, find_packages

setup(
    name='passport_mrz_extractor',
    version='1.0',
    description='A Python library for reading MRZ data from passport images using Tesseract OCR',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    author='Azimkozho Kenzhebek uulu',
    author_email='azimkozho.inventor@gmail.com',
    url='https://github.com/Azim-Kenzh/passport_mrz_extractor',
    license='MIT',  # License type
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'pytesseract',
        'opencv-python',
        'mrz',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Graphics :: Capture :: Scanners',
    ],
    python_requires='>=3.10',
    keywords='MRZ passport OCR Tesseract image-processing',
)
