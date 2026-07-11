---
title: "Fuse33 LiDAR Scan"
date: 2023-01-08
description: "Fast and easy 3D building scans: I recently used an iPhone 12 Pro( with LiDAR and the PolyCam( app to create a 3D scan of the shop floor at Fuse33, a"
author: "James"
program: general
categories:
  - "Great Projects"
  - "James"
  - "SteamHead Spaces"
image: "/images/2023/01/Screen-Shot-2023-01-08-at-3.30.32-PM.png"
imageAlt: "Fuse33 LiDAR Scan"
---

Fast and easy 3D building scans: I recently used an [iPhone 12 Pro](https://www.google.com/search?q=backmarket+iphone+12+pro&client=firefox-b-1-d&sxsrf=AJOqlzXqPJekMK40O36lIsz6TBxxnMf2fQ%3A1673215464954&ei=6D27Y9rzOcyWkPIP7JuG4AM&ved=0ahUKEwjah6-r_bj8AhVMC0QIHeyNATwQ4dUDCA8&uact=5&oq=backmarket+iphone+12+pro&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIICAAQFhAeEAoyBggAEBYQHjIICAAQFhAeEAoyBggAEBYQHjIGCAAQFhAeMgYIABAWEB46CggAEEcQ1gQQsAM6BAgjECc6DQguELEDEMcBENEDEEM6CAgAEIAEELEDOgsILhCDARCxAxCABDoICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToECAAQQzoICC4Q5QQQkQI6BQgAEJECOgsILhCxAxDHARDRAzoOCC4QgAQQsQMQxwEQ0QM6CAguEIAEELEDOgsILhCABBCxAxDUAjoKCAAQgAQQhwIQFDoHCAAQsQMQQzoNCAAQgAQQhwIQsQMQFDoLCAAQgAQQsQMQgwE6BwgAEIAEEAo6CQgAEBYQHhDxBEoECEEYAEoECEYYAFD9BlijKGDyKWgDcAF4AIABmAGIAYkSkgEEMjAuNJgBAKABAcgBCMABAQ&sclient=gws-wiz-serp) with LiDAR and the [PolyCam](https://poly.cam) app to create a 3D scan of the shop floor at Fuse33, a makerspace in Calgary. The resulting 3D data was composed of voxels, and the image was painted on from the iPhone's camera. It is blurry, but only took about 15 minutes!

While there are other methods for creating 3D scans that will give you a sharper image, such as photogrammetry and [Neural Radiance Fields](https://www.youtube.com/watch?v=vppnmLCrjVU) (NeRF), these methods require rendering the data on a graphics card after taking hundreds of photographs in good lighting conditions. You would need to schedule a whole day, maybe multiple days, for a model of this size to be completed. In contrast, the LiDAR method on the iPhone 12 Pro allows you to render the 3D model on the phone itself, simply by taking a long video. I am interested in using 3D models of spaces and environments for education. After some moderate successes during the pandemic, I feel that these spaces can help students empathize and relate to different environments differently than seeing text, photos, or even videos. The perspective is not forced, it's novel/exciting, and it hints at content creation inside virtual spaces. The physical spaces our students have access to varies widely, and avoiding those limitations is something I'm quite excited about but don't yet know how to fully take advantage of. <iframe style="height: 60vmin; width: 100%; max-height: 720px; max-width: 1280px; min-height: 280px; min-width: 280px;" title="polycam capture viewer" src="https://poly.cam/capture/888518EF-6D3B-4CD0-BA35-647FE2FBFEA6" frameborder="0"></iframe>In case the above embed does not load for you, here is the link: [https://poly.cam/capture/888518EF-6D3B-4CD0-BA35-647FE2FBFEA6](https://poly.cam/capture/888518EF-6D3B-4CD0-BA35-647FE2FBFEA6) Also here is the exterior of the building: [https://poly.cam/capture/66A2B978-2DA3-463C-BE29-8DF1C7AF287A](https://poly.cam/capture/66A2B978-2DA3-463C-BE29-8DF1C7AF287A) Some good resources:

-   https://www.reddit.com/r/photogrammetry/
-   https://www.reddit.com/r/3DScanning
-   https://poly.cam
-   For the latest in NeRF search for "Instant-NGP", but fyi it is not quite non-coder friendly yet. here is a simple explainer video though: https://www.youtube.com/watch?v=fvXOjV7EHbk
