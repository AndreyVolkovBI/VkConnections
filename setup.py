import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vkconnections",
    version="0.0.1",
    author="Andrey Volkov",
    author_email="andrey@volkov.tech",
    description="Finding the shortest path from one vk user to another through friends.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndreyVolkovBI/VkConnections",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)