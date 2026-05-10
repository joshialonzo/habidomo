#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


import click  # noqa: E402

from shared.repositories.sections_repository import (  # noqa: E402
    InMemorySectionsRepository,
)
from shared.service_layer.sections_service import SectionsService  # noqa: E402

# Dependency injection: create repository and service
repository = InMemorySectionsRepository()
service = SectionsService(repository)


@click.group()
def cli():
    """Habidomo Condominium Management CLI"""


@cli.group()
def sections():
    """Manage sections"""


@sections.command()
@click.option("--name", required=True, help="Section name")
@click.option("--description", help="Section description")
def create(name: str, description: str | None):
    """Create a new section"""
    try:
        section = service.create_section(name, description)
        click.echo(f"✓ Section created: {section.name} (ID: {section.section_id})")
    except ValueError as e:
        raise click.ClickException(str(e)) from e


@sections.command()
def list_sections():
    """List all sections"""
    sections_list = service.get_sections()
    if not sections_list:
        click.echo("INFO: No sections found")
        return

    click.echo("SECTIONS:")
    click.echo("-" * 80)
    for section in sections_list:
        click.echo(f"ID: {section.section_id}")
        click.echo(f"Name: {section.name}")
        click.echo(f"Description: {section.description or 'N/A'}")
        click.echo(f"Created: {section.created_at}")
        click.echo("-" * 80)


@sections.command()
@click.argument("section_id")
@click.option("--name", help="New section name")
@click.option("--description", help="New section description")
def update(section_id: str, name: str | None, description: str | None):
    """Update a section"""
    if name is None and description is None:
        raise click.UsageError("Must provide --name or --description to update")  # noqa: EM101, TRY003

    try:
        section = service.update_section(section_id, name, description)
        if section:
            click.echo(f"✓ Section updated: {section.name}")
        else:
            raise click.ClickException(f"Section with ID {section_id} not found")  # noqa: EM102, TRY003
    except ValueError as e:
        raise click.ClickException(str(e)) from e


@sections.command()
@click.argument("section_id")
def delete(section_id: str):
    """Delete a section"""
    if service.delete_section(section_id):
        click.echo("✓ Section deleted")
    else:
        raise click.ClickException(f"Section with ID {section_id} not found")  # noqa: EM102, TRY003


if __name__ == "__main__":
    cli()
