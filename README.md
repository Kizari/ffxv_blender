# FFXV Blender Utilities

An add-on for Blender that provides various utility functions to make working with FFXV assets easier.

Compatible with Blender 2.79 and later.

Please check back for updates from time to time. Any new functionality will be listed in the changelog at the bottom of this page.

# Installation

1. Click *Code > Download ZIP* at the top of this page.

2. Open *File > User Preferences* from inside Blender

3. Click *Install add-on from file* and select the downloaded ZIP archive

4. Check the box next to FFXV Utilities to enable the add-on

5. (Optional) click *Save User Settings* if you want the add-on to load automatically with Blender

# Features

Currently includes some utility functions for working with FFXV assets. If there is a feature missing you would like to see in the add-on, please open an Issue with the "enhancement" tag. If you have a script you already use yourself for FFXV modding that you feel would make a good addition to the add-on, feel free to attach it to the enhancement request or submit a pull request.

## Cleanup

**Empties**

Many assets will often have a ton of empty objects lovingly referred to as the "spiky mess." These are not required for mods to work, so can be safely deleted. The "Empties" button in the Cleanup panel will remove all of these in a single click.

**Unused Bones**

Most of the time, you won't need to use most of the bones in the FFXV rig, and they will simply get in the way and make your workflow much more tedious. Just be warned that this will delete all bones that don't have weights, so if there are extra bones you wish to keep in the armature, you may need to paint some weights on them first.

**Unused Vert. Groups**

When scrolling through the vertex groups list to paint weights on your model, it can be a real pain when there are a ton of extra groups to wade through that you don't even plan to use. Similar to Unused Bones, this will remove any vertex groups from the active mesh that don't have any associated weight values.

**Zero Weights**

Sometimes you have a vertex or two that is flying off into the distance for some unknown reason. You select it to check why, only to have to scroll down 2 pages of vertex groups looking for the ones that aren't zero. This function removes all those zero weight entries from all vertices in the active mesh.

## Animation

**Remove Translation**

This is used to stop your model running away while you're trying to watch the animation to see how the mesh responds to your weight painting. For the active action, this function will remove the translation from the chosen axis for each keyframe in the animation.

## Weight Tools

**Smooth Seams**

*Warning: this function can be a little slow, you may need to give it 20+ seconds to complete, especially on higher poly models*

Your model likely has 2 vertices sharing the same location along the seams of your mesh. Sometimes the model ends up in a state where the weights are slightly different between two vertices on the seam which can cause the seam to tear when animating. This is especially common when using the blur tool. It can also be a pain to fix due to the vertices sharing the same spot. This function simply averages the weights between these two vertices to smooth out the weights on the seams, similar to how the blur tool would work.

# Issues

If you encounter any problems with the add-on, please submit an Issue here with the appropriate tag. If you are able to include any error messages from Blender, and as much detail relevant to the project you were working on and what you were doing at the time the issue occured, that would help immensely.

# Contributing

Would be more than happy to include features or scripts from others that make FFXV mods to keep everything together in one place for the community. Scripts would be best submitted as an Issue with the "enhancement" tag, or a pull request. Alternatively, feel free to contact me directly and I can work with you to get it sorted.

# Changelog

**Version 1.0.0**
- Add-on released
