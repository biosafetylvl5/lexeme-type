# PROJECT

![Tests](.github/badges/tests-badge.svg)
![Coverage](.github/badges/coverage-badge.svg)
![Mypy](.github/badges/mypy-badge.svg)
![Ruff](.github/badges/ruff-badge.svg)
![Install](.github/badges/install-badge.svg)
![CSpell](.github/badges/cspell-badge.svg)
![Commitizen](.github/badges/commitizen-badge.svg)

[![GitHub stars](https://img.shields.io/github/stars/biosafetylvl5/PROJECT.svg)](https://github.com/biosafetylvl5/PROJECT/stargazers)

## Contributing

I welcome contributions to PROJECT!

Please follow these general guidelines:

1.  **Fork the repository** on GitHub.
2.  **Create a new branch** for your feature or bug fix. (eg. `git checkout -b feature/your-feature-name` or `fix/issue-number-description`)
3.  **Make your changes** and **ensure all linters and tests pass** (the CI will also check for you, but it's helpful to run them locally).
4.  **Commit your changes** using [Conventional Commits](https://www.conventionalcommits.org/) (see "Commit Messages" below).
5.  **Push your branch** to your fork.
6.  **Open a Pull Request** against the `main` (or `dev`) branch of the `biosafetylvl5/PROJECT` repository.
7.  Clearly describe your changes in the PR. If it fixes an open issue, please link to it (e.g., "Fixes #123").

If you're planning a larger contribution, it's a good idea to open an issue first to discuss your ideas so your work isn't duplicated/done in vain.

### Setting up Your Development Environment

#### Using Dev Containers (Recommended)

This repository is configured to use [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers). This is the recommended way to set up your development environment, as it ensures consistency and comes pre-configured with all necessary tools.

1.  Ensure you have Docker Desktop and the "Dev Containers" extension installed in VS Code.
2.  Clone the repository: `git clone https://github.com/biosafetylvl5/PROJECT.git`
3.  Open the cloned repository folder in VS Code. (You can also do this [without VS code](https://github.com/devcontainers/cli), but that's up to you to figure out.)
4.  VS Code should prompt you to "Reopen in Container". Click it.
    *   If it doesn't prompt, open the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and search for "Dev Containers: Reopen in Container".
5.  The dev container will build (this might take a few minutes the first time). Once built, VS Code will be connected to the containerized environment, with Python, Poetry, and all project dependencies (including development tools and plugins) already installed and configured.

### Running Tests

I use [pytest](https://docs.pytest.org/) for testing.

1.  **Run all tests**:
    ```bash
    poetry run pytest
    ```
    This will also generate a coverage report in the terminal and an XML report (`coverage.xml`).

2.  **Run tests with specific markers**:
    For example, to skip slow tests:
    ```bash
    poetry run pytest -m "not slow"
    ```

### Commit Messages

This project uses [Commitizen](https://commitizen-tools.github.io/commitizen/) with the `cz_conventional_commits` style. This helps create a more readable and structured commit history.

* **If using the Dev Container or after `poetry install --all-extras`**:
    You can use `cz c` or `git cz` (if hooks are set up) to be interactively guided through creating a commit message:
    ```bash
    poetry run cz commit
    # or simply if commitizen is on your PATH / using dev container
    # cz c
    ```
* **Manually**:
    Ensure your commit messages follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/).
    Example: `feat: add user authentication endpoint`
    Common types: `feat`, `fix`, `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`.

### Documentation

All substantial changes must be accompanied by a changelog release file. These can be created with [`brassy`](https://biosafetylvl5.github.io/brassy/) in `docs/source/release/latest` with `brassy -t $filename` or `brassy -t` to name the file after your current branch.

If your changes affect documentation or add new features that need documenting, please update the other documentation in the `docs/` directory. Documentation is built using Sphinx and brassy.
