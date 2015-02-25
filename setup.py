setup(
    name='commonUtils',
    version='0.0.1',
    description='common Utilities',
    url='https://github.com/XavierVal/commonUtils',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Development',
        'Framework :: Lettuce',
        'Intended Audience :: Developers',
        'Intended Audience :: Quality Assurance',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.7'
    ],
    py_modules=[
        'commonUtils.time_utils',
        'commonUtils.parsing_utils'
        ],
    packages=[
        'commonutils',
        'commonutils.mocks',
        'commonutils.templates',
        'commonutils.pageobjects'
        ],
)
