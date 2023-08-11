# Hello World AlgoKit Tealish Template

## What is this?

This is a template for [AlgoKit](https://github.com/algorandfoundation/algokit-cli) with the following features:

- A bare bones hello world smart contract written in Tealish
- A single Pytest test for the smart contract
- Relevant environment files set up
- AlgoKit Utils integration

Please note that this template is intended for the Web3 With Algorand course as part of the [Environment Setup](blocksauce.io/web3-with-algorand/fundamentals/environment-setup) lesson. This specific template has been intentionally kept simple and is not meant for use in production.

## How do I use this?

This template can be installed by the AlgoKit CLI. Here is an example command that installs this project non-interactively: `algokit init -n hello_world --template-url https://github.com/wenkanglu/algokit_tealish_template --UNSAFE-SECURITY-accept-template-url --git --bootstrap --answer template hello_world`.

Here is an explanation of the command:

- `init` is the command used to tell AlgoKit to initialise a new project from a template.
- `-n hello_world` provides the name of the project and its root directory.
- `--template-url` https://github.com/wenkanglu/algokit_tealish_template tells AlgoKit where to find the template.
- `--UNSAFE-SECURITY-accept-template-url` tells AlgoKit that you are accepting the risks associated with using a community-made template.
- `--git` tells AlgoKit to initialise a local git repository for the project.
- `--bootstrap` tells AlgoKit to install project dependencies after the template is set up.
- `--answer` template hello_world selects the 'hello_world' sub-template to be used for the project.

After installation, you can open up the project in your code editor and ensure that you are in the created virtual environment (`poetry shell` if you aren't). Then simply run `pytest` in your terminal to run the test.
