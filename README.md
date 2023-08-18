# AlgoKit Tealish Template

## Summary

This is an AlgoKit template that houses multiple Tealish projects intended for the Web3 With Algorand course by Block Sauce. The course is still in development but you can preview it [here](https://blocksauce.io).

## Disclaimer

Please note that this repository is under active development and the installation process and usage of this template may change without notice.

## Usage

Below is a guide on how to set up the "hello_world" project from this AlgoKit template. In accordance to best practices, please be sure to look through the source code before setting up any unofficial template projects like this.

1. Install [Algokit](https://github.com/algorandfoundation/algokit-cli#install).
2. Ensure that the "algokit_sandbox" Docker container is running. If not, run `algokit localnet start`.
3. In the directory where you want your project to be, run `algokit init -n hello_world --template-url https://github.com/wenkanglu/algokit_tealish_template --UNSAFE-SECURITY-accept-template-url --git --bootstrap --answer template hello_world`.
4. Open up the newly created project in VS Code.
5. If you don't yet have syntax highlighting for Tealish, right-click the "tealish-0.0.1.vsix" file and select Install Extension VSIX.
6. Run `poetry shell`, then run `pytest` once within the virtual environment.
