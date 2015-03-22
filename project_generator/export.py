# Copyright 2014-2015 0xc0170
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from .builder import ProjectBuilder

help = 'Export a project record'


def run(generator, settings, args, root):
    generator.default_settings(args, settings)
    generator.set_toolchain(args)
    generator.load_definitions(args.defdirectory)
    projects, project_paths = generator.run(args)

    if args.build:
        ProjectBuilder(settings).run(args, projects, project_paths, root)


def setup(subparser):
    subparser.add_argument("-f", "--file", help="YAML projects file")
    subparser.add_argument("-p", "--project", help="Project to be generated")
    subparser.add_argument(
        "-t", "--tool", help="Create project files for provided tool (uvision by default)")
    subparser.add_argument(
        "-b", "--build", action="store_true", help="Build defined projects")
    subparser.add_argument(
        "-defdir", "--defdirectory",
        help="Path to the definitions, otherwise default (~/.pg/definitions) is used")
