import setuptools

setuptools.setup(
    name="streamlit-plotly-events",
    version="0.0.1",
    author="Gabriel Menezes",
    description="Bi directional communication between Plotly and Streamlit",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        "streamlit >= 1.11.1",
        "plotly >= 5.15.0",
    ],
)
